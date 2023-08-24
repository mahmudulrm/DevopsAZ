provider "aws" {
  region = var.aws_region
}

// Create EC2
resource "aws_instance" "web" {
  ami = var.os
  key_name = "terraform_key" 
  instance_type = var.instance_type
  subnet_id = aws_subnet.demo-subnet.id
  vpc_security_group_ids = [aws_security_group.demo-pvc-sg.id]
  tags = {
    Name = "Web"
  }
}

// Create VPC
resource "aws_vpc" "demo-vpc" {
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = "demo-vpc"
  }
}

// Create Subnet

resource "aws_subnet" "demo-subnet" {
  vpc_id = aws_vpc.demo-vpc.id
  cidr_block = var.public_subnet_cidr_block
  map_public_ip_on_launch = true
  tags = {
    Name = "demo_subnet"
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


// Create subnet association

resource "aws_route_table_association" "demo-rt-ass" {
  subnet_id      = aws_subnet.demo-subnet.id
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