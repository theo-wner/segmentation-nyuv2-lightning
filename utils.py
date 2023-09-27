import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import os
import numpy as np

# Creates a tuple of image and GT mask
def visualize_img_gt(image, gt_mask, filename='test.png'):
    # Image
    # Convert Image from Tensor to Image
    image = image.permute(1, 2, 0).numpy()

    plt.figure(figsize=(16, 5))

    # Place Subplots
    # Leave everything as it is!!!
    # If then only adjust the wspace value!!!
    plt.subplots_adjust(left=0.005,
                        bottom=0,
                        right=0.84,
                        top=1,
                        wspace=0.75,
                        hspace=0.0)
    
    plt.subplot(1, 2, 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image)

    # Definde Labels and Colors as Dictionary
    labels_and_colors = {'Bett' : 'lightblue',
                         'Bücher' : 'brown',
                         'Decke' : 'lightyellow',
                         'Stuhl' : 'orange',
                         'Fußboden' : 'magenta',
                         'Möbel' : 'blue',
                         'Objekte' : 'green',
                         'Bild' : 'red',
                         'Sofa' : 'purple',
                         'Tisch' : 'goldenrod',
                         'Fernseher' : 'lightgreen',
                         'Wand' : 'gray',
                         'Fenster' : 'lightgray',
                         'Nicht annotiert' : 'white'}

    # Create Colormap from Dictionary
    cmap = mcolors.ListedColormap(list(labels_and_colors.values()))

    # Ground Truth Mask
    # Convert Mask from Tensor to Image
    gt_mask = gt_mask.squeeze().numpy()
    # Set Unlabeled Pixels to Value 14 (For the colormap)
    gt_mask[gt_mask == 255] = 14

    plt.subplot(1, 2, 2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(gt_mask, cmap=cmap, vmin=0, vmax=14)

    # Legend
    legend_elements = [mpatches.Patch(facecolor=labels_and_colors[label],
                             edgecolor='black',
                             label=label) for label in labels_and_colors]
    plt.legend(handles=legend_elements,
               loc='center left',
               bbox_to_anchor=(1, 0.5))
    
    # Set Legend Title
    plt.gca().get_legend().set_title('Annotationen')

    # Set the legend font size
    plt.gca().get_legend().get_title().set_fontsize('xx-large')
    
    # Make legend bold
    plt.setp(plt.gca().get_legend().get_title(), fontweight='bold')

    # Set the font size of the labels and font type
    for label in plt.gca().get_legend().get_texts():
        label.set_fontsize('xx-large')
        label.set_fontfamily('serif')

    # Make the font of my legend look like latex
    plt.gca().get_legend().get_title().set_fontfamily('serif')

    # Save Figure
    directory = './figures/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, filename))
    plt.close()


# Creates a triple of image, GT mask and segmented mask and saves it to directory figures
def visualize_img_gt_pr(image, gt_mask, pr_mask, filename='test.png'):
    # Image
    # Convert Image from Tensor to Image
    image = image.permute(1, 2, 0).numpy()

    plt.figure(figsize=(16, 5))

    # Place Subplots
    # Leave everything as it is!!!
    # If then only adjust the wspace value!!!
    plt.subplots_adjust(left=0.005,
                        bottom=0,
                        right=0.84,
                        top=1,
                        wspace=0.01,
                        hspace=0.0)
    
    plt.subplot(1, 3, 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image)

    # Definde Labels and Colors as Dictionary
    labels_and_colors = {'Bett' : 'lightblue',
                         'Bücher' : 'brown',
                         'Decke' : 'lightyellow',
                         'Stuhl' : 'orange',
                         'Fußboden' : 'magenta',
                         'Möbel' : 'blue',
                         'Objekte' : 'green',
                         'Bild' : 'red',
                         'Sofa' : 'purple',
                         'Tisch' : 'goldenrod',
                         'Fernseher' : 'lightgreen',
                         'Wand' : 'gray',
                         'Fenster' : 'lightgray',
                         'Nicht annotiert' : 'white'}

    # Create Colormap from Dictionary
    cmap = mcolors.ListedColormap(list(labels_and_colors.values()))

    # Ground Truth Mask
    # Convert Mask from Tensor to Image
    gt_mask = gt_mask.squeeze().numpy()
    # Set Unlabeled Pixels to Value 14 (For the colormap)
    gt_mask[gt_mask == 255] = 14

    plt.subplot(1, 3, 2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(gt_mask, cmap=cmap, vmin=0, vmax=14)

    # Prediction Truth Mask
    # Convert Mask from Tensor to Image
    pr_mask = pr_mask.squeeze().numpy()
    # Set Unlabeled Pixels to Value 14 (For the colormap)
    pr_mask[pr_mask == 255] = 14
    plt.subplot(1, 3, 3)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(pr_mask, cmap=cmap, vmin=0, vmax=14)

    # Legend
    legend_elements = [mpatches.Patch(facecolor=labels_and_colors[label],
                             edgecolor='black',
                             label=label) for label in labels_and_colors]
    plt.legend(handles=legend_elements,
               loc='center left',
               bbox_to_anchor=(1, 0.5))
    
    # Set Legend Title
    plt.gca().get_legend().set_title('Annotationen')

    # Set the legend font size
    plt.gca().get_legend().get_title().set_fontsize('xx-large')
    
    # Make legend bold
    plt.setp(plt.gca().get_legend().get_title(), fontweight='bold')

    # Set the font size of the labels and font type
    for label in plt.gca().get_legend().get_texts():
        label.set_fontsize('xx-large')
        label.set_fontfamily('serif')

    # Make the font of my legend look like latex
    plt.gca().get_legend().get_title().set_fontfamily('serif')

    # Save Figure
    directory = './figures/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, filename))
    plt.close()