<h1 align="center">🎉 gaussian-splatting-metric 🔥</h1>
<p align="center">
🍦 本仓库旨在为3DGS加速&压缩方向初学者提供一个全面的指标评测方法。本仓库展示了集成各种指标评测方法的3DGS官方代码示例。该方法也可被参考并应用到各种基于3DGS改进的代码框架中。 🍦</p>

> &emsp;&emsp;涵盖的指标有：
> 
> - 训练时间（Training time）；
> - 渲染帧率（FPS）；
> - 高斯数量（Gaussian Number）；
> - GPU峰值显存占用（Peak Memory）；
> 
> &emsp;&emsp;同时还支持：
> 
> - 高斯数量随训练迭代变化曲线绘制；

&emsp;&emsp;如果你想要集成该评测指标到其他3DGS方法上，请参考博客：[3DGS加速&压缩指标评测方法、高斯数量变化曲线绘制——Training Time、FPS、Gaussian Number、Peak Memory](https://blog.csdn.net/qq_60587145/article/details/157025583).

## 指标评测示例

&emsp;&emsp;以  `Tanks & Temples` 数据集的 `Train` 场景为例：

```bash
python train.py -m output/train-metric -s ./dataset/train --eval
python render.py -m output/train-metric --skip_train
python metrics.py -m output-train_metric
```

&emsp;&emsp;运行上述命令，得到如下结果。整理可得各项指标：

| Method | Scene | Training Time | #Gaussians | Peak Memory | FPS   | PSNR   | SSIM  | LPIPS |
| ------ | ----- | ------------- | ---------- | ----------- | ----- | ------ | ----- | ----- |
| 3DGS   | Train | 852.4s        | 1089691    | 6.814 GB    | 133.9 | 22.178 | 0.821 | 0.195 |

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/08d43630e6d34248bdb65bcd8e25071e.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6113e0524a9447da84263d3aca7f5170.png)

## 高斯数量变化曲线绘制

```bash
python draw_pic.py --csv_path /path/to/csv file
```

- csv file在运行`train.py`时得到，保存在模型路径（`-m`）下。

&emsp;&emsp;运行上述程序，得到对应的迭代曲线。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8f66cda947fe4f3fb35b7e8048d58a3a.png)

<p align="center">
🍦 如果你觉得该项目对你有用，请给作者一个 Star 🌟，不胜感激～～ 🍦</p>

