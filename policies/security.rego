package terraform.security

deny[msg] {
 input.resource.aws_security_group[_].ingress[_].cidr_blocks[_] == "0.0.0.0/0"
 msg := "security groups must not expose unrestricted ingress"
}

package kubernetes.security

deny[msg] {
 input.kind == "Deployment"
 input.spec.template.spec.containers[_].securityContext.privileged == true
 msg := "privileged containers are forbidden"
}

deny[msg] {
 input.kind == "Deployment"
 not input.spec.template.spec.containers[_].resources.requests
 msg := "resource requests are required"
}
