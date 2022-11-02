# Changelog

## [1.5.0.3] - 2022-11-02

* A new API for HeModel and PlainModel: includes support for training, multiple inputs/outputs.
* pyhelayers: added some missing HeConfigRequirement methods.
* MockupContext includes operation counts tracking.
* Tile tensors: rotate method now supports interleaved dimensions.
* Tile tensors: A new printing mode for tile tensor that prints tiles.

## [1.4.0.5] - 2022-07-19

* Fix a bug in which encode() and encode_encrypt() encoded Python lists of doubles as lists of integers.
* Allow XGBoost inference using HeModel interface.
* XGBoost demo notebook: use HeProfileOptimizer to find optimal packing configuration and context parameters; encrypt and decrypt using IoProcessor.

## [1.4.0.4] - 2022-06-27

* Fix bug in XGBoost inference when a tree has a single leaf node.

## [1.4.0.3] - 2022-06-21

* mltoolbox: Improve trainer API; add starting_point() helper

## [1.4.0.2] - 2022-06-13

* Add support for HEaaN on IBM Z (s390x)
* Bug fixes

## [1.4.0.1] - 2022-06-06

* 'accord' submodule in pyhelayers: MPC and ZK, including demo notebooks.
* 'mltoolbox' submodule in pyhelayers: convert a network to be HE friendly. Including a new demo notebook.
* ARIMA model training and prediction, including a new demo notebook.
* Added automatic bootstrapping to logistic regression training.
* Upgraded to HEaaN 3.5.0.
* Added support for Batch Normalization layer in NN.
* Added optimization of rotation keys in HE models: optimizer to detect and include only the necessary rotation keys in the HE context.
* New demo notebook for deep neural networks: AlexNet, SqueezeNet and ResNet-18.
* New demo notebook for FHE XGBoost inference over the iris dataset.

## [1.3.0] - 2022-04-03

* Support for HEaaN as backend
* Added helayerslite - a basic version of the library.
* helayerslite compiled for WASM (Web assembly)
* Faster logistic regression training
* Support for convolution with custom padding
