# Output block to display important information about the resources
output "instance_public_ip" {
  value = aws_instance.web.public_ip
}

output "instance_private_ip" {
  value = aws_instance.web.private_ip
}

output "instance_ssh_command" {
  value = "ssh ec2-user@${aws_instance.web.public_ip}"
}