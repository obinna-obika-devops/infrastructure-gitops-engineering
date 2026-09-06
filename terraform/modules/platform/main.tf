variable "name" { type = string }
variable "subnet_ids" { type = list(string) }
variable "tags" { type = map(string) }

resource "aws_security_group" "platform" {
  name   = "${var.name}-platform"
  vpc_id = data.aws_subnet.selected.vpc_id
  egress { from_port = 0 to_port = 0 protocol = "-1" cidr_blocks = ["0.0.0.0/0"] }
  tags = var.tags
}

data "aws_subnet" "selected" { id = var.subnet_ids[0] }

resource "aws_cloudwatch_log_group" "platform" {
  name              = "/platform/${var.name}"
  retention_in_days = 30
  tags              = var.tags
}

output "security_group_id" { value = aws_security_group.platform.id }
