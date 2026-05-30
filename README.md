C:\Users\29124\Desktop\Python_code\.venv\Scripts\python.exe D:\Python\dectrypto\006\q\crawl\2_5月24日_食堂菜品营养预测模型\main.py 
New https://pypi.org/project/ultralytics/8.4.57 available  Update with 'pip install -U ultralytics'
Ultralytics 8.4.53  Python-3.13.7 torch-2.9.1+cu126 CUDA:0 (NVIDIA GeForce RTX 4050 Laptop GPU, 6140MiB)
engine\trainer: agnostic_nms=False, amp=True, angle=1.0, augment=True, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=True, cutmix=0.0, data=data.yaml, degrees=10, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, end2end=None, epochs=30, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolov8n.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=foods_model, nbs=64, nms=False, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=8, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=D:\Python\dectrypto\006\q\crawl\2_524_\runs\detect\foods_model, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=0, workspace=None
Overriding model.yaml nc=80 with nc=17

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]             
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]             
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               
  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]                 
 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]                  
 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]                 
 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]                 
 22        [15, 18, 21]  1    754627  ultralytics.nn.modules.head.Detect           [17, 16, None, [64, 128, 256]]
Model summary: 130 layers, 3,014,163 parameters, 3,014,147 gradients, 8.2 GFLOPs

Transferred 319/355 items from pretrained weights
Freezing layer 'model.22.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
AMP: checks passed 
train: Fast image access  (ping: 0.30.3 ms, read: 27.510.0 MB/s, size: 13.3 KB)
train: Scanning D:\Python\dectrypto\006\q\crawl\2_5月24日_食堂菜品营养预测模型\dataset\labels\train... 700 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 700/700 1.7Kit/s 0.4s
train: New cache created: D:\Python\dectrypto\006\q\crawl\2_524_\dataset\labels\train.cache
val: Fast image access  (ping: 0.10.0 ms, read: 38.417.1 MB/s, size: 13.8 KB)
val: Scanning D:\Python\dectrypto\006\q\crawl\2_5月24日_食堂菜品营养预测模型\dataset\labels\val... 191 images, 1 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 192/192 2.4Kit/s 0.1s
val: New cache created: D:\Python\dectrypto\006\q\crawl\2_524_\dataset\labels\val.cache
optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... 
optimizer: AdamW(lr=0.000476, momentum=0.9) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias(decay=0.0)
Plotting labels to D:\Python\dectrypto\006\q\crawl\2_524_\runs\detect\foods_model\labels.jpg... 
Image sizes 640 train, 640 val
Using 0 dataloader workers
Logging results to D:\Python\dectrypto\006\q\crawl\2_524_\runs\detect\foods_model
Starting training for 30 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       1/30      1.09G      1.461      4.015      1.825          4        640: 100% ━━━━━━━━━━━━ 88/88 3.5it/s 24.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 3.3it/s 3.7s
                   all        192        205     0.0141      0.884      0.102     0.0412

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       2/30      1.29G      1.389      3.408       1.73          4        640: 100% ━━━━━━━━━━━━ 88/88 3.8it/s 23.5s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s
                   all        192        205      0.235      0.345      0.178      0.073

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       3/30      1.31G      1.474      2.983      1.774          4        640: 100% ━━━━━━━━━━━━ 88/88 4.0it/s 22.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s
                   all        192        205      0.292      0.429      0.329      0.125

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       4/30      1.31G      1.463      2.654      1.745          4        640: 100% ━━━━━━━━━━━━ 88/88 5.3it/s 16.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.4it/s 1.6s
                   all        192        205      0.372      0.546      0.468      0.199

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       5/30      1.31G       1.43      2.469      1.732          4        640: 100% ━━━━━━━━━━━━ 88/88 5.6it/s 15.6s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.1it/s 1.7s
                   all        192        205      0.496      0.594      0.526      0.209

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       6/30      1.31G      1.432      2.301      1.723          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 16.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.596      0.542      0.584      0.281

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       7/30      1.31G        1.4      2.186      1.681          4        640: 100% ━━━━━━━━━━━━ 88/88 5.6it/s 15.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 6.9it/s 1.8s
                   all        192        205      0.635      0.564      0.647      0.313

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       8/30      1.31G      1.412      2.076      1.697          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 16.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.4it/s 1.6s
                   all        192        205      0.576      0.584      0.616      0.315

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       9/30      1.31G      1.364       1.92      1.671          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 16.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.608      0.607      0.647      0.299

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      10/30      1.31G      1.396      1.901      1.646          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 15.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.633      0.692      0.692      0.351

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      11/30      1.31G      1.344      1.799      1.615          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 16.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.741       0.67      0.735      0.389

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      12/30      1.31G      1.347      1.793      1.624          4        640: 100% ━━━━━━━━━━━━ 88/88 5.4it/s 16.2s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 6.4it/s 1.9s
                   all        192        205      0.692      0.677      0.717       0.38

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      13/30      1.31G      1.316      1.712      1.599          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 15.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.4it/s 1.6s
                   all        192        205      0.679      0.695      0.713      0.357

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      14/30      1.31G      1.297      1.645      1.589          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 16.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.642      0.741      0.739       0.37

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      15/30      1.31G      1.292      1.611      1.602          4        640: 100% ━━━━━━━━━━━━ 88/88 5.6it/s 15.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.716      0.734      0.749      0.376

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      16/30      1.31G      1.285      1.544      1.576          4        640: 100% ━━━━━━━━━━━━ 88/88 5.5it/s 15.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.4it/s 1.6s
                   all        192        205      0.735      0.639      0.733      0.374

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      17/30      1.31G      1.251      1.475      1.559          4        640: 100% ━━━━━━━━━━━━ 88/88 5.6it/s 15.8s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 6.9it/s 1.7s
                   all        192        205      0.781      0.707      0.763      0.397

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      18/30      1.31G      1.244       1.41      1.531          4        640: 100% ━━━━━━━━━━━━ 88/88 5.1it/s 17.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 6.5it/s 1.9s
                   all        192        205      0.747      0.765      0.779      0.414

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      19/30      1.31G       1.22      1.382      1.528          4        640: 100% ━━━━━━━━━━━━ 88/88 5.2it/s 17.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.3it/s 1.7s
                   all        192        205      0.768      0.774      0.787      0.394

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      20/30      1.31G      1.207      1.336      1.508          4        640: 100% ━━━━━━━━━━━━ 88/88 5.6it/s 15.7s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.3it/s 1.6s
                   all        192        205      0.789      0.743      0.786       0.39
Closing dataloader mosaic

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      21/30      1.31G      1.188      1.716      1.708          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 14.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.4it/s 1.6s
                   all        192        205      0.817      0.665      0.761      0.393

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      22/30      1.31G      1.139      1.521       1.66          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 13.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.3it/s 1.6s
                   all        192        205      0.766      0.772      0.782      0.419

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      23/30      1.31G      1.122      1.464      1.605          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 14.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.838      0.778      0.798      0.435

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      24/30      1.31G      1.105      1.382      1.598          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 13.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 6.9it/s 1.7s
                   all        192        205       0.82      0.757      0.802      0.433

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      25/30      1.31G      1.093      1.349      1.581          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 14.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.3it/s 1.6s
                   all        192        205       0.83      0.739        0.8      0.424

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      26/30      1.31G      1.085       1.34      1.585          4        640: 100% ━━━━━━━━━━━━ 88/88 6.2it/s 14.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.876      0.728      0.805      0.435

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      27/30      1.31G      1.081      1.314       1.58          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 14.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.2it/s 1.7s
                   all        192        205      0.858      0.741      0.801      0.424

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      28/30      1.31G      1.055      1.311      1.558          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 14.1s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.3it/s 1.6s
                   all        192        205      0.847      0.754      0.797      0.422

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      29/30      1.31G      1.041      1.315      1.559          4        640: 100% ━━━━━━━━━━━━ 88/88 6.3it/s 13.9s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.5it/s 1.6s
                   all        192        205      0.843      0.742        0.8       0.43

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      30/30      1.31G      1.024      1.275      1.525          4        640: 100% ━━━━━━━━━━━━ 88/88 6.2it/s 14.3s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 7.1it/s 1.7s
                   all        192        205      0.856      0.736      0.802      0.429

30 epochs completed in 0.153 hours.
Optimizer stripped from D:\Python\dectrypto\006\q\crawl\2_524_\runs\detect\foods_model\weights\last.pt, 6.3MB
Optimizer stripped from D:\Python\dectrypto\006\q\crawl\2_524_\runs\detect\foods_model\weights\best.pt, 6.3MB

Validating D:\Python\dectrypto\006\q\crawl\2_524_\runs\detect\foods_model\weights\best.pt...
Ultralytics 8.4.53  Python-3.13.7 torch-2.9.1+cu126 CUDA:0 (NVIDIA GeForce RTX 4050 Laptop GPU, 6140MiB)
Model summary (fused): 73 layers, 3,008,963 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 12/12 4.1it/s 2.9s
                   all        192        205      0.832      0.787      0.827      0.463
                           14         14          1       0.66      0.962      0.655
                            12         12          1      0.857      0.915      0.606
                            16         16      0.827        0.6      0.843      0.404
                             15         15      0.765      0.733      0.704      0.368
                             12         25      0.795       0.62      0.757      0.287
                          12         12      0.903      0.779      0.923      0.565
                            10         10      0.981        0.5      0.758      0.441
                           10         10      0.773        0.8      0.875      0.487
                           10         10      0.793        0.9      0.923      0.453
                            10         10      0.826        0.7      0.672       0.31
                           10         10          1      0.791      0.801      0.406
                           10         10      0.674        0.7      0.671      0.274
                            10         10      0.762          1      0.875      0.502
                          10         10      0.726        0.9      0.806      0.562
                           10         10      0.746          1      0.943      0.547
                            10         11      0.606       0.84      0.645      0.434
                          10         10      0.966          1      0.995      0.579
Speed: 0.2ms preprocess, 7.6ms inference, 0.0ms loss, 1.1ms postprocess per image
Results saved to D:\Python\dectrypto\006\q\crawl\2_524_\runs\detect\foods_model

进程已结束，退出代码为 0
