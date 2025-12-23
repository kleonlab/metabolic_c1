#!/usr/bin/env python3
"""
Script to examine the variable dimensions pickle file from a pretrained model.
"""

import pickle
import sys
from pathlib import Path
from typing import Any


def examine_pkl(pkl_path: str) -> None:
    """Load and examine the contents of a pickle file."""
    
    pkl_file = Path(pkl_path)
    
    if not pkl_file.exists():
        print(f"Error: File not found: {pkl_path}")
        sys.exit(1)
    
    print(f"Examining: {pkl_path}")
    print("=" * 80)
    
    try:
        with open(pkl_file, 'rb') as f:
            data = pickle.load(f)
        
        # Print basic information
        print(f"\nData Type: {type(data)}")
        print(f"Data Size: {sys.getsizeof(data)} bytes")
        
        # Examine based on data type
        if isinstance(data, dict):
            print(f"\nNumber of keys: {len(data)}")
            print("\n" + "=" * 80)
            print("Dictionary Contents:")
            print("=" * 80)
            
            for key, value in data.items():
                print(f"\nKey: {key}")
                print(f"  Type: {type(value)}")
                
                if hasattr(value, 'shape'):
                    print(f"  Shape: {value.shape}")
                    print(f"  Dtype: {value.dtype}")
                elif hasattr(value, '__len__') and not isinstance(value, str):
                    print(f"  Length: {len(value)}")
                    if len(value) > 0:
                        print(f"  First element type: {type(value[0])}")
                        if hasattr(value[0], 'shape'):
                            print(f"  First element shape: {value[0].shape}")
                else:
                    print(f"  Value: {value}")
        
        elif isinstance(data, list):
            print(f"\nList length: {len(data)}")
            if len(data) > 0:
                print(f"First element type: {type(data[0])}")
                if hasattr(data[0], 'shape'):
                    print(f"First element shape: {data[0].shape}")
                print("\n" + "=" * 80)
                print("List Contents (first 10 items):")
                print("=" * 80)
                for i, item in enumerate(data[:10]):
                    print(f"\nIndex {i}:")
                    print(f"  Type: {type(item)}")
                    if hasattr(item, 'shape'):
                        print(f"  Shape: {item.shape}")
                        print(f"  Dtype: {item.dtype}")
                    else:
                        print(f"  Value: {item}")
        
        elif hasattr(data, 'shape'):
            print(f"\nShape: {data.shape}")
            print(f"Dtype: {data.dtype}")
            print(f"\nArray statistics:")
            print(f"  Min: {data.min()}")
            print(f"  Max: {data.max()}")
            print(f"  Mean: {data.mean()}")
            print(f"  Std: {data.std()}")
        
        else:
            print(f"\nData content:\n{data}")
        
        print("\n" + "=" * 80)
        print("Examination complete!")
        print("=" * 80)
        
    except Exception as e:
        print(f"\nError loading pickle file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        pkl_path = sys.argv[1]
    else:
        # Default path
        pkl_path = "/storage/home/hcoda1/0/amete7/r-agarg35-0/vla/st/assets/ST-Tahoe/var_dims.pkl"
    
    examine_pkl(pkl_path)


if __name__ == "__main__":
    main()

"""
output for ST-Tahoe:
================================================================================

Data Type: <class 'dict'>
Data Size: 360 bytes

Number of keys: 8

================================================================================
Dictionary Contents:
================================================================================

Key: input_dim
  Type: <class 'int'>
  Value: 2000

Key: gene_dim
  Type: <class 'numpy.int64'>
  Shape: ()
  Dtype: int64

Key: hvg_dim
  Type: <class 'int'>
  Value: 2000

Key: output_dim
  Type: <class 'int'>
  Value: 2000

Key: pert_dim
  Type: <class 'int'>
  Value: 1138

Key: gene_names
  Type: <class 'numpy.ndarray'>
  Shape: (2000,)
  Dtype: object

Key: batch_dim
  Type: <class 'int'>
  Value: 14

Key: pert_names
  Type: <class 'list'>
  Length: 1138
  First element type: <class 'numpy.str_'>
  First element shape: ()

================================================================================
Examination complete!
================================================================================
"""