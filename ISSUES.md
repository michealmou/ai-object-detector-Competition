Below are ready-to-post GitHub issues for the competition repository. You can copy-paste these into GitHub issues or run `create_issues.py`.

1) Dataset: Download & Verify classroom dataset

Steps:
- Download the provided dataset from Google Drive (link in competition).
- Inspect `data.yaml` and confirm class names match expected behavior labels.
- Quick checks: count images per class, check for corrupted files.

Checklist:
- [ ] Download dataset
- [ ] Open `data.yaml` and verify class names
- [ ] Report any missing/corrupted files

Hints:
- Use Google Drive UI or `gdown` to download.
- `data.yaml` contains the class names; map them carefully to behaviors.

---

2) Data preparation: split and convert annotations

Steps:
- Split dataset into `train/val/test`.
- Convert annotations to the YOLO format required by your chosen version.

Checklist:
- [ ] Create `train/val/test` splits
- [ ] Convert annotations if needed
- [ ] Verify shapes and labels look correct

Hints:
- Beginners: start with a small subset (e.g., 100 images) to test pipeline.
- Use scripts to automate conversions and seed `random` for reproducibility.

---

3) Colab: Create training notebook with T4 GPU

Steps:
- Create a Google Colab notebook for training.
- Set Runtime → Change runtime type → GPU → T4.
- Mount Google Drive and copy dataset there or stream from Drive.

Checklist:
- [ ] Notebook created
- [ ] Runtime set to T4 GPU
- [ ] Drive mount + checkpoint save code added

Hints:
- Save checkpoints frequently to Drive (e.g., every epoch or every N steps).
- Use smaller batch sizes if you get OOM errors.

---

4) Training: run experiments and save checkpoints to Drive

Steps:
- Run training in Colab.
- Save best and last checkpoints to Drive regularly.
- Log hyperparameters and results (learning rate, epochs, batch size).

Checklist:
- [ ] Run baseline experiment
- [ ] Save checkpoints to Drive
- [ ] Record hyperparameters and training curves

Hints:
- Use `torch.save()` or framework-native checkpointing.
- If disconnected, restart and resume from last checkpoint.

---

5) Evaluation & Inference: compute metrics and test on validation set

Steps:
- Evaluate the trained model on the validation set.
- Compute mAP, per-class precision/recall, and confusion matrix.
- Run a few inference examples and visualize predictions.

Checklist:
- [ ] Compute mAP and per-class metrics
- [ ] Produce visualized example predictions
- [ ] Save evaluation results to `results/`

Hints:
- For beginners: use existing evaluation scripts from YOLO repos and adapt class names from `data.yaml`.

---

6) Submission: package `your_team_name.pt` and upload

Steps:
- After finalizing the best checkpoint, rename it to `your_team_name.pt`.
- Upload to the Submission folder provided by the competition.

Checklist:
- [ ] Identify best checkpoint
- [ ] Rename to `your_team_name.pt`
- [ ] Upload to submission folder before deadline

Hints:
- Keep a copy of `data.yaml` and a short README explaining how to run inference with your model.

---

7) Project: Beginner guide and role assignments (team of 3)

Steps:
- Assign roles among the 3 team members.
- Keep notes of who does which task and timelines.

Checklist:
- [ ] Assign roles (Dataset, Training/Colab, Evaluation & Submission)
- [ ] Create a shared Google Drive for checkpoints
- [ ] Set a short daily sync time

Hints and roles suggestion:
- Member A (Dataset): Download dataset, verify `data.yaml`, prepare splits.
- Member B (Training): Build Colab notebook, run training, manage checkpoints.
- Member C (Evaluation/Sub): Evaluate model, prepare `your_team_name.pt` and upload.

Beginner tips:
- Keep experiments simple: one change at a time.
- Use small subsets to test code before full training.
- Document commands and dependencies in a README.
