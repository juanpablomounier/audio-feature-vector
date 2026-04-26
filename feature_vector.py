""" 
Here feature and feature vector classes are declared.
"""

import math

#CLASSES

class Feature:
    def __init__(self, name, raw_value, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.normalized_value = None

        if isinstance(name, (str)):
            self.name = name
        else:
            raise ValueError("Name must be string type.")
        
        if isinstance(raw_value, (int, float)):
            self.raw_value = raw_value
            #self.normalized_value = self.normalize()
        else:
            raise ValueError("Raw value must be numeric type.")
    

    def __str__(self):
        return f"{self.name}: {self.raw_value}"
    

    def normalize(self):
        if self.min_value == self.max_value:
            self.normalized_value = 0.0
        else:
            self.normalized_value = (self.raw_value - self.min_value) / (self.max_value - self.min_value)

    


class FeatureVector:
    def __init__(self):
        self.vector = []
        self.allowed_features = ["ZCR", "SpectralEntropy", "CrestFactor", "Energy", "Novelty"]


    def __str__(self):
        return f"{self.vector}"

        
    def __repr__(self):
        return f"FeatureVector({self.to_vector()})"


    def add_feature(self, feature):
        if not feature.name in self.allowed_features:
            raise ValueError("Feature must be allowed.")
        for f in self.vector:
            if feature.name == f.name:
                raise ValueError(f"Vector already has {f.name}")
        if isinstance(feature, (Feature)):
            self.vector.append(feature)
        else:
            raise ValueError("feature must be an instance of Feature.")
    

    def normalize_features(self):
        for feature in self.vector:
            feature.normalize()
        

    def to_vector(self):
        values_vector = []
        for f in self.allowed_features:
            found = False
            for feature in self.vector:
                if f == feature.name:
                    if feature.normalized_value is None:
                        raise ValueError("Features must be normalized first")
                    else:
                        values_vector.append(feature.normalized_value)
                        found = True
                    break
            if not found:
                values_vector.append(0.0)
        
        return values_vector
    

    def dimension(self):
        return len(self.allowed_features)
  

    def print_vector(self):
        print("El vector tiene los siguientes valores: ")
        print(self.to_vector())


    def _validate_other(self, other):
        if not isinstance(other, FeatureVector):
            raise ValueError("Other vector must be an instance of FeatureVector")
        if other.dimension() != self.dimension():
            raise ValueError("Other vector must have R5 dimension.")
    

    def distance_to(self, other):
        self._validate_other(other)
        vector1 = self.to_vector()
        vector2 = other.to_vector()
        suma = 0

        for x, y in zip(vector1, vector2):
            suma += (x - y) ** 2
        
        return math.sqrt(suma)
    
  
    def cosine_similarity(self, other):
        self._validate_other(other)
        vector1 = self.to_vector()
        vector2 = other.to_vector()
        dot = 0
        norm1 = 0
        norm2 = 0
        
        for x, y in zip(vector1, vector2):
            dot += x*y

        for x in vector1:
            norm1 += x**2

        for y in vector2:
            norm2 += y**2

        norm1 = math.sqrt(norm1)
        norm2 = math.sqrt(norm2)

        if norm1 == 0 or norm2 == 0:
            raise ValueError("Cannot compute cosine similarity with zero vector")

        return dot / (norm1 * norm2)

        



#TESTING
vector1 = FeatureVector()
vector1.add_feature(Feature("ZCR", 0.4, 0, 1))
vector1.add_feature(Feature("Novelty", 0.2, 0, 1))
vector1.add_feature(Feature("Energy", 35.0, 0, 100))
vector1.add_feature(Feature("SpectralEntropy", 0.8, 0, 1))
vector1.add_feature(Feature("CrestFactor", 7.7, 1, 10))

vector1.normalize_features()
vector1.to_vector()
vector1.print_vector()

vector2 = FeatureVector()
vector2.add_feature(Feature("ZCR", 0.2, 0, 1))
vector2.add_feature(Feature("Novelty", 0.6, 0, 1))
vector2.add_feature(Feature("Energy", 59.0, 0, 100))
vector2.add_feature(Feature("SpectralEntropy", 0.3, 0, 1))
vector2.add_feature(Feature("CrestFactor", 3.5, 1, 10))

vector2.normalize_features()
vector2.to_vector()
vector2.print_vector() 

distance = vector1.distance_to(vector2)
print(f"La distancia entre ambos vectores es: {distance}")

distance = vector2.distance_to(vector1)
print(f"La distancia entre ambos vectores es: {distance}")

similarity = vector1.cosine_similarity(vector2)
print(f"La similaridad entre ambos vectores es: {similarity}")

similarity = vector2.cosine_similarity(vector1)
print(f"La similaridad entre ambos vectores es: {similarity}")