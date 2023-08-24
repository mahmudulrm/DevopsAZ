variable "aws_region" {
  default     = "us-east-1"
}

variable "os" {
  default = "ami-0f34c5ae932e6f0e4"
}

variable "vpc_cidr_block" {
  description = "The CIDR block for the VPC."
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr_block" {
  description = "The CIDR block for the public subnet."
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr_block" {
  description = "The CIDR block for the private subnet."
  default     = "10.0.2.0/24"
}

variable "instance_type" {
  description = "The EC2 instance type."
  default     = "t2.micro"
}
