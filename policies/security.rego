package security

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

deny[msg] {
  input.kind == "Deployment"
  not input.spec.template.spec.containers[_].resources.limits
  msg := "resource limits are required"
}
