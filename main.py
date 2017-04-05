import docker
client = docker.from_env()


print("#### Container - Run ####")
container_alpine = client.containers.run("alpine", ["echo", "hello", "world"])
print(container_alpine)


print("#### Container - Run Background ####")
container = client.containers.run("bfirsh/reticulate-splines", detach=True)


print("#### Containers - List ####")
for container in client.containers.list():
  print(container.id)
  #container.stop()


print("#### Containers - Logs ####")
container = client.containers.get('e8515a63d16c')
print(container.logs())


print("#### Images - Api ####")
for image in client.images.list():
    print(image.id)


print("#### Images - Pull ####")
image = client.images.pull("alpine")
print(image.id)


print("#### Container commit as Image ####")
container = client.run("alpine", ["touch", "/helloworld"], detached=True)
container.wait()
image = container.commit("helloworld")
