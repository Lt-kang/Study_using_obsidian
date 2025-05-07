PaddleOCR text detection model 관련 추론을 진행할 때
cuda 관련 issue가 발생하였다.

```
(venv) PS C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main> python C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\tools\infer\predict_det.py --image_dir=C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\0_input-sample --det_algorithm="EAST" --det_model_dir=C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\output\test\inference
[2025/03/31 03:04:01] ppocr WARNING: The first GPU is used for inference by default, GPU ID: 0
Traceback (most recent call last):
  File "C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\tools\infer\predict_det.py", line 440, in <module>
    dt_boxes, _ = text_detector(img)
                  ^^^^^^^^^^^^^^^^^^
  File "C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\tools\infer\predict_det.py", line 396, in __call__
    dt_boxes, elapse = self.predict(img)
                       ^^^^^^^^^^^^^^^^^
  File "C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\tools\infer\predict_det.py", line 255, in predict
    self.predictor.run()
OSError: (External) CUDNN error(9), CUDNN_STATUS_NOT_SUPPORTED.
  [Hint: 'CUDNN_STATUS_NOT_SUPPORTED'.  The functionality requested is not presently supported by cuDNN.  ] (at C:\home\workspace\Paddle\paddle\phi\kernels\fusion\gpu\fused_conv2d_add_act_kernel.cu:618)
  [operator < fused_conv2d_add_act > error]
```

나로서는 혼자 해결할 수가 없었기에 PaddleOCR discussion탭을 확인하여 다른 사람들의 해결방법을 확인했다.

해당 이슈를 해결한 대부분의 사람들은 구버전을 사용하고 있었다. 
나는 3.0.0 버전을 사용하고 있었기에

2.6.1 버전으로 다운그레이드하여 다시 시도해보았다.


단, 이번에는 새로운 에러가 발생하였다.
```
(venv) PS C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main> python C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\tools\infer\predict_det.py --image_dir=C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\0_input-sample --det_algorithm="EAST" --det_model_dir=C:\Users\Xenrose\Desktop\paddleocr\PaddleOCR-main\output\test\inference
[2025/03/31 03:19:20] ppocr WARNING: The first GPU is used for inference by default, GPU ID: 0
Could not locate zlibwapi.dll. Please make sure it is in your library path!
```

`zlibwapi.dll` 파일 관련 이슈였다.
해당 이슈는 다행이게도 한글로 자료를 올려주신 분들이 많아서 쉽게 해결할 수 있었다.

ref: https://ecogis.net/entry/%EC%A5%AC%ED%94%BC%ED%84%B0-%EB%85%B8%ED%8A%B8%EB%B6%81-%EC%BB%A4%EB%84%90-%EB%8D%B0%EB%93%9Czlibwapidll-%ED%8C%8C%EC%9D%BC-%EB%B0%9C%EC%83%9D-%EC%8B%9C-%ED%95%B4%EA%B2%B0%EB%B2%95

주피터 커널 이슈를 해결하는 방법이지만
해당 벙법을 사용하면 바로 위 이슈도 해결이 가능하다.


https://forums.developer.nvidia.com/t/could-not-load-library-cudnn-cnn-infer64-8-dll-error-code-193/218437/16
위 링크에서 `zlib123dllx64.zip` 파일을 다운받고
zlibwapi.dll 파일을 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin 폴더에 옮겨놓으면 된다.


결과적으로 text detection 모델의 inference가 정상적으로 진행됨을 확인하였다.
