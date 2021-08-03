from pixellib.instance import instance_segmentation
import os

def object_detection(img_path, output_path):
	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
	segment_image = instance_segmentation()
	segment_image.load_model('handlers/recognize/mask_rcnn_coco.h5')

	target_class = segment_image.select_target_classes(person = True)

	result = segment_image.segmentImage(
		image_path = img_path,
		segment_target_classes = target_class,
		extract_segmented_objects = True,
		save_extracted_objects = True,
		output_image_name = output_path
	)

	return len(result[0]['scores'])