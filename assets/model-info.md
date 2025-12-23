```
About to call trainer.fit() with manual checkpoint...

================================================================================
CHECKING DECODER WEIGHTS INITIALIZATION
================================================================================
PyTorch nn.Linear default: Kaiming Uniform initialization
  weights ~ U(-sqrt(1/fan_in), sqrt(1/fan_in))
  Expected std = sqrt(1/(3*fan_in))

decoder.0.weight:
  Shape: (1024, 2000)
  Mean: -0.000010, Std: 0.012909
  Range: [-0.022361, 0.022361]
  Expected init std: 0.012910
  Expected init bound: ±0.022361
  Std ratio: 1.000
  ⚠️  WARNING: Very close to initialization! Likely NOT trained.

decoder.4.weight:
  Shape: (1024, 1024)
  Mean: -0.000015, Std: 0.018035
  Range: [-0.031250, 0.031250]
  Expected init std: 0.018042
  Expected init bound: ±0.031250
  Std ratio: 1.000
  ⚠️  WARNING: Very close to initialization! Likely NOT trained.

decoder.8.weight:
  Shape: (512, 1024)
  Mean: 0.000001, Std: 0.018041
  Range: [-0.031250, 0.031250]
  Expected init std: 0.018042
  Expected init bound: ±0.031250
  Std ratio: 1.000
  ⚠️  WARNING: Very close to initialization! Likely NOT trained.

decoder.12.weight:
  Shape: (2000, 512)
  Mean: -0.000003, Std: 0.025507
  Range: [-0.044194, 0.044194]
  Expected init std: 0.025516
  Expected init bound: ±0.044194
  Std ratio: 1.000
  ⚠️  WARNING: Very close to initialization! Likely NOT trained.

================================================================================
⚠️⚠️⚠️  DECODER APPEARS UNTRAINED  ⚠️⚠️⚠️
All decoder layers show statistics consistent with initialization.
================================================================================
```