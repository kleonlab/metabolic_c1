# General Info

## Competition Support Set Statistics

| Dataset            | Samples | Cells    | Samples/Cell Ratio |
|-------------------|--------:|--------:|-------------------:|
| competition_train |     942 | 221,273 |             0.0043 |
| k562_gwps         |     526 | 111,605 |             0.0047 |
| jurkat            |     126 |  21,412 |             0.0059 |
| rpe1              |     127 |  22,317 |             0.0057 |
| k562              |     101 |  18,465 |             0.0055 |
| hepg2             |      92 |   9,386 |             0.0098 |
| **TOTAL**         | **1,914** | **404,458** |         **0.0047** |

## Training Configuration

- **Cell set length**: 256 cells per sample
- **Batch size**: 64 samples
- **Steps per epoch**: 29 (1,914 samples ÷ 64 batch size)

### Processing Per Iteration

- **Per step**: 64 samples × 256 cells = **16,384 cells**
- **Per epoch**: 29 steps × 16,384 = **~475k cell observations**

> Note: Cell observations exceed total cell count due to sampling with replacement for control cells and data augmentation

## Pretrained Tahoe Model Info

### Perturbation Features File
```
SUMMARY:
  Total keys: 1138
  Value types distribution:
    - Tensor: 1138
  Unique tensor shapes: {(1138,)}

  Sample of all keys (first 10 and last 10):
    - [('(R)-Verapamil (hydrochloride)', 0.05, 'uM')]
    - [('(R)-Verapamil (hydrochloride)', 0.5, 'uM')]
    - [('(R)-Verapamil (hydrochloride)', 5.0, 'uM')]
    - [('(S)-Crizotinib', 0.05, 'uM')]
    - [('(S)-Crizotinib', 0.5, 'uM')]
    - [('(S)-Crizotinib', 5.0, 'uM')]
    - [('18β-Glycyrrhetinic acid', 0.05, 'uM')]
    - [('18β-Glycyrrhetinic acid', 0.5, 'uM')]
    - [('18β-Glycyrrhetinic acid', 5.0, 'uM')]
    - [('4EGI-1', 0.05, 'uM')]
    ... (1118 more keys) ...
    - [('palbociclib', 5.0, 'uM')]
    - [('venetoclax', 0.05, 'uM')]
    - [('venetoclax', 0.5, 'uM')]
    - [('venetoclax', 5.0, 'uM')]
    - [('vincristine', 0.05, 'uM')]
    - [('vincristine', 0.5, 'uM')]
    - [('vincristine', 5.0, 'uM')]
    - [('γ-Oryzanol', 0.05, 'uM')]
    - [('γ-Oryzanol', 0.5, 'uM')]
    - [('γ-Oryzanol', 5.0, 'uM')]
```