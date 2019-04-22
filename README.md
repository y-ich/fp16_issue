# reproduction code of issue https://github.com/apple/coremltools/issues/351

## Usage

```
git clone https://github.com/y-ich/fp16_issue.git
pipenv install
pipenv shell
curl -O https://dl.dropboxusercontent.com/s/13p8x0acarz9bwx/ELFOpenGo_v2.mlmodel
convert.py
predict.py
```