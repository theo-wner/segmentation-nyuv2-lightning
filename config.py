import argparse

parser = argparse.ArgumentParser(description='Parser')

parser.add_argument('--num_classes', type=int, default=13)
parser.add_argument('--num_epochs', type=int, default=2000)
parser.add_argument('--devices', type=int, default=0)
parser.add_argument('--path_to_checkpoint', type=str, default=None)
parser.add_argument('--cpu', type=bool, default=False)

args = parser.parse_args()

IGNORE_INDEX = 255
NUM_CLASSES = args.num_classes
BATCH_SIZE = 16
NUM_WORKERS = 4
NUM_EPOCHS = args.num_epochs
DEVICES = [args.devices]
CPU_USAGE = args.cpu
CHECKPOINT = args.path_to_checkpoint

# Command for training 13 classes with checkpoint:
# python train.py --num_classes 13 --num_epochs 2000 --devices 1 --path_to_checkpoint ./tb_logs/nyuv2_13_classes/version_0/checkpoints/epoch=999-step=50000.ckpt

# Command for tensorboard:
# tensorboard --logdir tb_logs/ --bind_all