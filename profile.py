import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"
node.routable_control_ip = True  # boolean, not string

# Update + install Apache, then start and verify it's running
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt-get update -y"))
node.addService(rspec.Execute(shell="/bin/sh", command="DEBIAN_FRONTEND=noninteractive sudo apt-get install -y apache2"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo systemctl enable --now apache2"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo systemctl is-active apache2"))  # exits 0 only if 'active'

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()

