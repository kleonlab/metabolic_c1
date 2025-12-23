#!/usr/bin/env python3
"""
Script to examine the pert_onehot_map.pt file
"""

import torch
import sys
from pathlib import Path

def examine_pt_file(filepath):
    """Examine a PyTorch .pt file and print its structure and contents"""
    
    print(f"Examining file: {filepath}")
    print("=" * 80)
    
    try:
        # Load the file
        # Note: weights_only=False is needed for files containing numpy objects
        # This is safe for trusted internal files
        data = torch.load(filepath, map_location='cpu', weights_only=False)
        
        # Print type information
        print(f"\nTop-level type: {type(data)}")
        print(f"Top-level type name: {type(data).__name__}")
        
        # Handle different data types
        if isinstance(data, dict):
            print(f"\nDictionary with {len(data)} keys:")
            print("-" * 80)
            
            # Show first few keys as examples
            num_examples = min(5, len(data))
            print(f"\nShowing first {num_examples} keys as examples:")
            
            for i, (key, value) in enumerate(data.items()):
                if i >= num_examples:
                    break
                    
                print(f"\nKey {i+1}: {key}")
                print(f"  Type: {type(value).__name__}")
                
                if isinstance(value, torch.Tensor):
                    print(f"  Shape: {value.shape}")
                    print(f"  Dtype: {value.dtype}")
                    print(f"  Device: {value.device}")
                    print(f"  Min: {value.min().item() if value.numel() > 0 else 'N/A'}")
                    print(f"  Max: {value.max().item() if value.numel() > 0 else 'N/A'}")
                    print(f"  Mean: {value.float().mean().item() if value.numel() > 0 else 'N/A'}")
                    
                    # Print a sample of the data if it's small enough
                    if value.numel() <= 20:
                        print(f"  Data:\n{value}")
                    else:
                        print(f"  First few elements: {value.flatten()[:10]}")
                        
                elif isinstance(value, (list, tuple)):
                    print(f"  Length: {len(value)}")
                    if len(value) > 0:
                        print(f"  First element type: {type(value[0]).__name__}")
                        if len(value) <= 10:
                            print(f"  Contents: {value}")
                        else:
                            print(f"  First 10 elements: {value[:10]}")
                            
                elif isinstance(value, dict):
                    print(f"  Nested dictionary with {len(value)} keys: {list(value.keys())[:10]}")
                    
                else:
                    # For other types, try to print the value if it's small
                    value_str = str(value)
                    if len(value_str) <= 200:
                        print(f"  Value: {value}")
                    else:
                        print(f"  Value (truncated): {value_str[:200]}...")
            
            # Print summary statistics
            print(f"\n{'=' * 80}")
            print("SUMMARY:")
            print(f"  Total keys: {len(data)}")
            
            # Analyze all keys to provide summary
            key_types = {}
            tensor_shapes = set()
            for key, value in data.items():
                key_type = type(value).__name__
                key_types[key_type] = key_types.get(key_type, 0) + 1
                if isinstance(value, torch.Tensor):
                    tensor_shapes.add(tuple(value.shape))
            
            print(f"  Value types distribution:")
            for vtype, count in key_types.items():
                print(f"    - {vtype}: {count}")
            
            if tensor_shapes:
                print(f"  Unique tensor shapes: {tensor_shapes}")
            
            # Check for "non-targeting" key
            print(f"\n  Checking for 'non-targeting' key:")
            if "non-targeting" in data:
                print(f"    ✓ Found 'non-targeting' key!")
                nt_value = data["non-targeting"]
                print(f"    Type: {type(nt_value).__name__}")
                if isinstance(nt_value, torch.Tensor):
                    print(f"    Shape: {nt_value.shape}")
                    print(f"    Dtype: {nt_value.dtype}")
                    print(f"    Data: {nt_value}")
            else:
                print(f"    ✗ 'non-targeting' key NOT found")
                # Check for similar keys
                similar_keys = [k for k in data.keys() if 'non' in str(k).lower() or 'target' in str(k).lower() or 'control' in str(k).lower() or 'dmso' in str(k).lower()]
                if similar_keys:
                    print(f"    Similar keys found: {similar_keys[:10]}")
            
            # Show a few more example keys
            print(f"\n  Sample of all keys (first 10 and last 10):")
            all_keys = list(data.keys())
            for key in all_keys[:10]:
                print(f"    - {key}")
            if len(all_keys) > 20:
                print(f"    ... ({len(all_keys) - 20} more keys) ...")
            if len(all_keys) > 10:
                for key in all_keys[-10:]:
                    print(f"    - {key}")
                        
        elif isinstance(data, torch.Tensor):
            print("\nTensor information:")
            print("-" * 80)
            print(f"  Shape: {data.shape}")
            print(f"  Dtype: {data.dtype}")
            print(f"  Device: {data.device}")
            print(f"  Number of elements: {data.numel()}")
            
            if data.numel() > 0:
                print(f"  Min: {data.min().item()}")
                print(f"  Max: {data.max().item()}")
                print(f"  Mean: {data.float().mean().item()}")
                
                if data.numel() <= 100:
                    print(f"\nFull tensor:\n{data}")
                else:
                    print(f"\nFirst few elements:\n{data.flatten()[:20]}")
                    print(f"\nLast few elements:\n{data.flatten()[-20:]}")
                    
        elif isinstance(data, (list, tuple)):
            print(f"\n{type(data).__name__} with {len(data)} elements:")
            print("-" * 80)
            
            for i, item in enumerate(data[:10]):  # Show first 10 items
                print(f"\nElement {i}:")
                print(f"  Type: {type(item).__name__}")
                if isinstance(item, torch.Tensor):
                    print(f"  Shape: {item.shape}")
                    print(f"  Dtype: {item.dtype}")
                else:
                    item_str = str(item)
                    if len(item_str) <= 200:
                        print(f"  Value: {item}")
                    else:
                        print(f"  Value (truncated): {item_str[:200]}...")
                        
            if len(data) > 10:
                print(f"\n... and {len(data) - 10} more elements")
                
        else:
            print(f"\nData content:")
            print("-" * 80)
            data_str = str(data)
            if len(data_str) <= 1000:
                print(data)
            else:
                print(f"{data_str[:1000]}...")
                
        print("\n" + "=" * 80)
        print("Examination complete!")
        
    except Exception as e:
        print(f"\nError loading file: {e}")
        import traceback
        traceback.print_exc()
        return 1
        
    return 0

if __name__ == "__main__":
    # Get the script's directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Default file path
    default_file = project_root / "assets" / "ST-Tahoe" / "pert_onehot_map.pt"
    
    # Allow custom file path as argument
    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
    else:
        filepath = default_file
    
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
        
    sys.exit(examine_pt_file(filepath))

