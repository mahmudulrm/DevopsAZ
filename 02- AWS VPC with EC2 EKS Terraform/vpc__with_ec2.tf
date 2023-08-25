provider "aws" {
  region = var.aws_region
}

# Create EC2
resource "aws_instance" "web" {
  ami = var.os
  key_name = "terraform_key" 
  instance_type = var.instance_type
  subnet_id = aws_subnet.demo-subnet-1.id
  vpc_security_group_ids = [aws_security_group.demo-pvc-sg.id]
  tags = {
    Name = "eks"
  }
}

# Create VPC
resource "aws_vpc" "demo-vpc" {
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = "demo-vpc"
  }
}

# Create Subnet 1

resource "aws_subnet" "demo-subnet-1" {
  vpc_id = aws_vpc.demo-vpc.id
  cidr_block = var.public_subnet1_cidr_block
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a"
  tags = {
    Name = "demo_subnet-1"
  }
}

// Create Subnet 2

resource "aws_subnet" "demo-subnet-2" {
  vpc_id = aws_vpc.demo-vpc.id
  cidr_block = var.public_subnet2_cidr_block
  availability_zone = "us-east-1b"
  map_public_ip_on_launch = true
  tags = {
    Name = "demo_subnet-2"
  }
}


// Create Internet gatway
resource "aws_internet_gateway" "demo-igw" {
  vpc_id = aws_vpc.demo-vpc.id

  tags = {
    Name = "demo-igw"
  }
}

// Create Route Tabes
resource "aws_route_table" "demo-rt" {
  vpc_id = aws_vpc.demo-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.demo-igw.id
  }

  tags = {
    Name = "demo-rt"
  }
}


// Create subnet association 1

resource "aws_route_table_association" "demo-rt-ass-1" {
  subnet_id      = aws_subnet.demo-subnet-1.id
  route_table_id = aws_route_table.demo-rt.id
}

// Create subnet association 2

resource "aws_route_table_association" "demo-rt-ass-2" {
  subnet_id      = aws_subnet.demo-subnet-2.id
  route_table_id = aws_route_table.demo-rt.id
}


// Create security Group

resource "aws_security_group" "demo-pvc-sg" {
  name        = "demo-pvc-sg"
  vpc_id      = aws_vpc.demo-vpc.id

  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "demo-pvc-sg"
  }
}

module "sgs" {
  source = "./sg_eks"
  vpc_id = aws_vpc.demo-vpc.id
}

module "eks" {
  source = "./eks"
  sg_ids = module.sgs.security_group_public
  vpc_id = aws_vpc.demo-vpc.id
  
  subnet_ids = [
    aws_subnet.demo-subnet-2.id,
    aws_subnet.demo-subnet-1.id
  ]
  }
