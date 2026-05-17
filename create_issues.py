import os
import sys
import requests

# Usage:
# 1) set environment variables:
#    - GITHUB_TOKEN (your personal access token)
#    - GITHUB_REPO (owner/repo, e.g. your-org/your-repo)
# 2) python create_issues.py

TOKEN = os.environ.get('GITHUB_TOKEN')
REPO = os.environ.get('GITHUB_REPO')

if not TOKEN or not REPO:
    print("Missing GITHUB_TOKEN or GITHUB_REPO environment variable.")
    print("Set them and re-run. Example (PowerShell):")
    print("  $env:GITHUB_TOKEN='...'; $env:GITHUB_REPO='owner/repo'; python .\\create_issues.py")
    sys.exit(1)

HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github+json'
}

issues = [
    {
        'title': 'Dataset: Download & Verify classroom dataset',
        'body': 'Steps:\n- Download the provided dataset from Google Drive (link in competition).\n- Inspect `data.yaml` and confirm class names match expected behavior labels.\n- Quick checks: count images per class, check for corrupted files.\n\nChecklist:\n- [ ] Download dataset\n- [ ] Open `data.yaml` and verify class names\n- [ ] Report any missing/corrupted files\n\nHints:\n- Use Google Drive UI or `gdown` to download.\n- `data.yaml` contains the class names; map them carefully to behaviors.'
    },
    {
        'title': 'Data preparation: split and convert annotations',
        'body': 'Steps:\n- Split dataset into `train/val/test`.\n- Convert annotations to the YOLO format required by your chosen version.\n\nChecklist:\n- [ ] Create `train/val/test` splits\n- [ ] Convert annotations if needed\n- [ ] Verify shapes and labels look correct\n\nHints:\n- Beginners: start with a small subset (e.g., 100 images) to test pipeline.\n- Use scripts to automate conversions and seed `random` for reproducibility.'
    },
    {
        'title': 'Colab: Create training notebook with T4 GPU',
        'body': 'Steps:\n- Create a Google Colab notebook for training.\n- Set Runtime → Change runtime type → GPU → T4.\n- Mount Google Drive and copy dataset there or stream from Drive.\n\nChecklist:\n- [ ] Notebook created\n- [ ] Runtime set to T4 GPU\n- [ ] Drive mount + checkpoint save code added\n\nHints:\n- Save checkpoints frequently to Drive (e.g., every epoch or every N steps).\n- Use smaller batch sizes if you get OOM errors.'
    },
    {
        'title': 'Training: run experiments and save checkpoints to Drive',
        'body': 'Steps:\n- Run training in Colab.\n- Save best and last checkpoints to Drive regularly.\n- Log hyperparameters and results (learning rate, epochs, batch size).\n\nChecklist:\n- [ ] Run baseline experiment\n- [ ] Save checkpoints to Drive\n- [ ] Record hyperparameters and training curves\n\nHints:\n- Use `torch.save()` or framework-native checkpointing.\n- If disconnected, restart and resume from last checkpoint.'
    },
    {
        'title': 'Evaluation & Inference: compute metrics and test on validation set',
        'body': 'Steps:\n- Evaluate the trained model on the validation set.\n- Compute mAP, per-class precision/recall, and confusion matrix.\n- Run a few inference examples and visualize predictions.\n\nChecklist:\n- [ ] Compute mAP and per-class metrics\n- [ ] Produce visualized example predictions\n- [ ] Save evaluation results to `results/`\n\nHints:\n- For beginners: use existing evaluation scripts from YOLO repos and adapt class names from `data.yaml`.'
    },
    {
        'title': 'Submission: package `your_team_name.pt` and upload',
        'body': 'Steps:\n- After finalizing the best checkpoint, rename it to `your_team_name.pt`.\n- Upload to the Submission folder provided by the competition.\n\nChecklist:\n- [ ] Identify best checkpoint\n- [ ] Rename to `your_team_name.pt`\n- [ ] Upload to submission folder before deadline\n\nHints:\n- Keep a copy of `data.yaml` and a short README explaining how to run inference with your model.'
    },
    {
        'title': 'Project: Beginner guide and role assignments (team of 3)',
        'body': 'Steps:\n- Assign roles among the 3 team members.\n- Keep notes of who does which task and timelines.\n\nChecklist:\n- [ ] Assign roles (Dataset, Training/Colab, Evaluation & Submission)\n- [ ] Create a shared Google Drive for checkpoints\n- [ ] Set a short daily sync time\n\nHints and roles suggestion:\n- Member A (Dataset): Download dataset, verify `data.yaml`, prepare splits.\n- Member B (Training): Build Colab notebook, run training, manage checkpoints.\n- Member C (Evaluation/Sub): Evaluate model, prepare `your_team_name.pt` and upload.\n\nBeginner tips:\n- Keep experiments simple: one change at a time.\n- Use small subsets to test code before full training.\n- Document commands and dependencies in a README.'
    }
]

API_BASE = f'https://api.github.com/repos/{REPO}/issues'

for issue in issues:
    resp = requests.post(API_BASE, headers=HEADERS, json=issue)
    if resp.status_code == 201:
        print(f"Created issue: {issue['title']}")
    else:
        print(f"Failed to create issue: {issue['title']}")
        print(resp.status_code, resp.text)

print('Done.')
