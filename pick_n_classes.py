import os
import shutil

with open('identity_CelebA.txt', 'r') as file:
    lines = file.readlines()

num_classes = 100

image_names = [[] for x in range(num_classes)]

for line in lines:
    name = line.split(" ")[0]
    label = line.split(" ")[1].split("\n")[0]
    label = int(label)

    if label <= num_classes:
        image_names[label - 1].append(name)


image_dir = 'img_align_celeba/img_align_celeba'

for i in range(num_classes):

    # new directory to copy images to
    new_dir = 'data/{}'.format(i+1)

    # create new directory if it doesn't exist
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # loop through image names
    for name in image_names[i]:
        # construct path to image
        path_to_image = os.path.join(image_dir, name)
        #print(path_to_image, i)

        # check if image exists
        if os.path.exists(path_to_image):
            # construct path to new location
            new_location = os.path.join(new_dir, name)

            # copy image to new location
            shutil.copy2(path_to_image, new_location)