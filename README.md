# Audio Feature Vector Representation

This project implements a structured representation of audio features as a mathematical vector in ℝ⁵, along with similarity metrics for comparison.

## Overview

The goal of this project is to transform high-level audio features into a normalized vector space and enable comparison between different audio samples using mathematical metrics.

The system is composed of two main abstractions:

- **Feature**: represents a single measurable property (e.g., ZCR, Energy)
- **FeatureVector**: represents an ordered collection of features mapped into a fixed-dimensional vector space

---

## Feature Space Definition

The vector space is defined as:

[ZCR, SpectralEntropy, CrestFactor, Energy, Novelty]

Each feature is normalized to the range [0, 1] before being projected into the vector.

Missing features are automatically filled with `0.0`.

---

## Architecture

### Feature

Represents a single feature with:

- `name`: identifier
- `raw_value`: original value
- `min_value`, `max_value`: normalization bounds
- `normalized_value`: computed value

Normalization is performed using:

(x - min) / (max - min)

---

### FeatureVector

Encapsulates:

- A list of `Feature` objects
- A fixed feature ordering (ℝ⁵ space)

Provides:

- Feature validation (no duplicates, allowed features only)
- Normalization pipeline
- Vector projection
- Similarity metrics

---

## Methods

### add_feature(feature)
Adds a feature to the vector.

### normalize_features()
Applies normalization to all features.

### to_vector()
Returns the normalized vector representation.

Example:
[0.4, 0.8, 0.74, 0.35, 0.2]

---

### distance_to(other)
Computes Euclidean distance between two vectors.

### cosine_similarity(other)
Computes cosine similarity between two vectors.

- 1 → identical direction
- 0 → orthogonal (no similarity)

---

## Example Usage

```python
vector1 = FeatureVector()
vector1.add_feature(Feature("ZCR", 0.4, 0, 1))
vector1.add_feature(Feature("Energy", 35.0, 0, 100))
vector1.add_feature(Feature("CrestFactor", 7.7, 1, 10))
vector1.add_feature(Feature("SpectralEntropy", 0.8, 0, 1))
vector1.add_feature(Feature("Novelty", 0.2, 0, 1))

vector1.normalize_features()

vector2 = FeatureVector()
# ... same process ...

distance = vector1.distance_to(vector2)
similarity = vector1.cosine_similarity(vector2)
```

---

## Key Concepts

This project is based on:

- Vector space representation
- Feature normalization
- Euclidean distance
- Cosine similarity

It models audio data as points in a metric space, enabling comparison and similarity analysis.

---

## Scope

This project focuses on:

- Data representation
- Mathematical modeling
- Object-oriented design

It does **not** include:

- Audio signal processing (DSP extraction)
- Machine learning models
- External libraries (NumPy, etc.)

---

## Future Extensions

- Weighted features
- Alternative similarity metrics
- Integration with real audio feature extraction
- Application to other domains (e.g., text analysis)

---

## Author

Developed as part of a portfolio project focused on mathematical modeling and structured data representation.
