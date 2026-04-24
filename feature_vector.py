""" 
Here feature and feature vector classes are declared.
"""
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
    
  

    def print_vector(self):
        print("El vector tiene los siguientes valores: ")
        print(self.to_vector())
    



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