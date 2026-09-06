package security

import rego.v1

deny contains msg if {
  input.kind == "Deployment"
  some container in input.spec.template.spec.containers
  object.get(container.securityContext, "privileged", false) == true
  msg := "privileged containers are forbidden"
}

deny contains msg if {
  input.kind == "Deployment"
  some container in input.spec.template.spec.containers
  not container.resources.requests
  msg := "resource requests are required"
}

deny contains msg if {
  input.kind == "Deployment"
  some container in input.spec.template.spec.containers
  not container.resources.limits
  msg := "resource limits are required"
}

deny contains msg if {
  input.kind == "Deployment"
  some container in input.spec.template.spec.containers
  object.get(container.securityContext, "allowPrivilegeEscalation", true) != false
  msg := "allowPrivilegeEscalation must be false"
}

deny contains msg if {
  input.kind == "Deployment"
  some container in input.spec.template.spec.containers
  object.get(container.securityContext, "readOnlyRootFilesystem", false) != true
  msg := "readOnlyRootFilesystem must be true"
}

deny contains msg if {
  input.kind == "Deployment"
  some container in input.spec.template.spec.containers
  endswith(container.image, ":latest")
  msg := "mutable latest image tag is forbidden"
}
