provider "aws" {
  region = "us-west-2"
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "python101-${var.ws_name}"
  cidr = "10.0.0.0/16"

  azs             = ["us-west-2b"]
  public_subnets  = ["10.0.1.0/24"]
  private_subnets = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true

  tags = {
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
  }
}

resource "aws_security_group" "router_ports" {
  name = "allow_router_ports"
  description = "Allow port 22 and 830 for the python 101 workshop"
  vpc_id = "${module.vpc.vpc_id}"

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 830
    to_port = 830
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
    Name = "python101-${var.ws_name}"
  }
}

data "aws_ami" "juniper_vmx" {
  most_recent = true
  owners = ["679593333241"]
  
  filter {
    name = "name"
    values = ["vmx-nested-18.*-payg-*"]
  }
}

resource "aws_network_interface" "router_int_mgmt" {
  count = "${var.num_students}"
  subnet_id = "${module.vpc.public_subnets[0]}"
  security_groups = ["${aws_security_group.router_ports.id}"]

  tags = {
    Name = "vmx-student-mgmt-${count.index + 1}"
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
  }
}

resource "aws_eip" "mgmt_int" {
  count = "${var.num_students}"
  vpc = true
  network_interface = "${aws_network_interface.router_int_mgmt[count.index + 0].id}"

  tags = {
    Name = "vmx-student-mgmt-${count.index + 1}"
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
  }
}

locals {
  inventory_file = templatefile("${path.module}/inventory",
    {
      public_ips = "${aws_eip.mgmt_int.*.public_ip}",
      ssh_key_name = "${var.ssh_key_name}"
    }
  )
}

resource "local_file" "inventory" {
  content = "${local.inventory_file}"
  filename = "${path.module}/inventory-${var.ws_name}"
}


resource "aws_network_interface" "router_int1" {
  count = "${var.num_students}"
  subnet_id = "${module.vpc.private_subnets[0]}"
  security_groups = ["${aws_security_group.router_ports.id}"]

  tags = {
    Name = "vmx-student-int1-${count.index + 1}"
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
  }
}

resource "aws_network_interface" "router_int2" {
  count = "${var.num_students}"
  subnet_id = "${module.vpc.private_subnets[1]}"
  security_groups = ["${aws_security_group.router_ports.id}"]

  tags = {
    Name = "vmx-student-int2-${count.index + 1}"
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
  }
}

resource "aws_network_interface" "router_int3" {
  count = "${var.num_students}"
  subnet_id = "${module.vpc.private_subnets[2]}"
  security_groups = ["${aws_security_group.router_ports.id}"]

  tags = {
    Name = "vmx-student-int3-${count.index + 1}"
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
  }
}

resource "aws_instance" "vmx" {
  count = "${var.num_students}"
  ami = "${data.aws_ami.juniper_vmx.id}"
  instance_type = "m4.xlarge"
  key_name = "${var.ssh_key_name}"
  user_data = "${file("juniper-config-template.txt")}"

  network_interface {
    device_index = 0
    network_interface_id = "${aws_network_interface.router_int_mgmt[count.index + 0].id}"
  }

  network_interface {
    device_index = 1
    network_interface_id = "${aws_network_interface.router_int1[count.index + 0].id}"
  }
  network_interface {
    device_index = 2
    network_interface_id = "${aws_network_interface.router_int2[count.index + 0].id}"
  }
  network_interface {
    device_index = 3
    network_interface_id = "${aws_network_interface.router_int3[count.index + 0].id}"
  }

  tags = {
    Name = "vmx-student-${count.index + 1}"
    Terraform = "true"
    Workshop = "python101-${var.ws_name}"
  }
}
