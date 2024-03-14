import waterz as wz
import numpy as np

from chunkflow.lib.cartesian_coordinate import Cartesian 
from chunkflow.chunk import Chunk
from chunkflow.volume import load_chunk_or_volume
from chunkflow.volume import PrecomputedVolume, AbstractVolume

"""                  
affinity_paths = ["/mnt/home/mpaez/ceph/affsmaptrain/train1/affstrain1_vol1.h5", 
                  "/mnt/home/mpaez/ceph/affsmaptrain/train2/affstrain2_vol1.h5", 
                  "/mnt/home/mpaez/ceph/affsmaptrain/train3/affstrain3_vol1.h5", 
                  "/mnt/home/mpaez/ceph/affsmaptrain/train4/affstrain4_vol1.h5",
                  "/mnt/home/mpaez/ceph/affsmaptrain/train5/affstrain5_vol1.h5", 
                  "/mnt/home/mpaez/ceph/affsmaptrain/train6/affstrain6_vol1.h5", 
                  "/mnt/home/mpaez/ceph/affsmaptrain/train7/affstrain7_vol1.h5", 
                  "/mnt/home/mpaez/ceph/affsmaptrain/train8/affstrain8_vol1.h5", 
                  "/mnt/home/mpaez/ceph/affsmaptrain/train9/affstrain9_vol1.h5" ]
"""

class segment_methodology():
    def __init__(self, 
                 affinity_paths: list,
                 ground_truth_paths: list):
    
        super().__init__()
        self.affinity_paths = affinity_paths
        self.ground_truth_paths = ground_truth_paths

    @classmethod
    def agglomerate(self, affs_paths, gt_paths, **kwargs):
        segmentations = []
        
        # aff_thresholds = [0.005, 0.995]
        seg_thresholds = [0.1, 0.3, 0.6]

        for aff_path, gt_path in zip(affs_paths, gt_paths): 
            affs = load_chunk_or_volume(aff_path, **kwargs) 
            gt = load_chunk_or_volume(gt_paths, **kwargs) 

            assert affs.shape[-3:] == gt.shape[-3:]

            segmentation = wz.agglomerate(affs, seg_thresholds, gt=gt, 
                                          fragments=None, aff_threshold_low=0.0001, 
                                          aff_threshold_high=0.9999, return_merge_history=True, 
                                          return_region_graph=False)
            segmentations.append(segmentation) 

        return segmentations
    
    @classmethod
    def evaluate(self, affs_paths, gt_paths, **kwargs):
        segmentations = []
        
        seg_thresholds = [0.1, 0.3, 0.6]
        for aff_path, gt_path in zip(affs_paths, gt_paths): 
            affs = load_chunk_or_volume(aff_path, **kwargs) 
            gt = load_chunk_or_volume(gt_paths, **kwargs) 

            assert affs.shape[-3:] == gt.shape[-3:]

            # segmentation = wz.evaluate(ground_truth, affinity)
            segmentations.append(segmentation) 

        return segmentations

if __name__ == '__main__':

    affs_paths = ["/mnt/home/mpaez/ceph/affsmaptrain/experim/affstrain1_vol1.h5",
                  "/mnt/home/mpaez/ceph/affsmaptrain/train1/affstrain1_vol1.h5"]

    gt_paths = ["/mnt/ceph/users/neuro/wasp_em/jwu/40_gt/12_wasp_sample2/vol_07338/affs_160k.h5", 
                      "/mnt/ceph/users/neuro/wasp_em/jwu/40_gt/12_wasp_sample2/vol_07338/affs_160k.h5"]

    segmentation = segment_methodology.agglomerate(affs_paths, gt_paths) 

    for seg in segmentation:
        seg 



