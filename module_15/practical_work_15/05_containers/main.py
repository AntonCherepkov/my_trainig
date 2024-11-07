list_containers = []
num_containers = int(input('Enter the number of containers: '))

print()
for container in range(num_containers):
    while True:
        container_weight = int(input('Enter the weight of the container: '))
        if container == 0 or list_containers[container - 1] > container_weight:
            list_containers.append(container_weight)
            break
        else:
            print(f'The weight of this container should be less {list_containers[container - 1]}')

print(f'The positions of containers in the warehouse: {list_containers}')

new_list_container = []
new_container = int(input('Enter the weight of the new container: '))

for container in range(num_containers):
    if new_container > list_containers[container]:
        new_list_container.append(new_container)
        new_list_container.append(list_containers[container])
        print(f'Position of the new container: {container + 1}')
        new_container = 0
    else:
        new_list_container.append(list_containers[container])

print(f'The positions of containers in the warehouse: {new_list_container}')

# зачет!
