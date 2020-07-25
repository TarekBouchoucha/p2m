dvc run -n resnetunet \
-d data/training_patches/patches/ \
-d data/training_patches/training_indices.json \
-d data/training_patches/annotations/ \
-o checkpoint/ \
-o data/experiments/resnetunet/ \
"python run_training.py --seed=11 --gpu=1 --save-images=1 --model-name=resnetunet --group=resnetunet_post_fire_model --save-path=data/post_fire_model/"

