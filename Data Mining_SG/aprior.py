from itertools import combinations
from collections import defaultdict

class AprioriAlgorithm:
    def __init__(self, min_support=0.5, min_confidence=0.5):
        """
        Initialize Apriori algorithm
        
        Args:
            min_support (float): Minimum support threshold (0-1)
            min_confidence (float): Minimum confidence threshold (0-1)
        """
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.transactions = []
        self.frequent_itemsets = {}
        self.association_rules = []
    
    def load_transactions(self, transactions):
        """
        Load transaction data
        
        Args:
            transactions (list): List of transactions, where each transaction is a list of items
        """
        self.transactions = [frozenset(transaction) for transaction in transactions]
        self.num_transactions = len(self.transactions)
    
    def get_support(self, itemset):
        """
        Calculate support for an itemset
        
        Args:
            itemset (frozenset): Set of items
            
        Returns:
            float: Support value (0-1)
        """
        count = sum(1 for transaction in self.transactions if itemset.issubset(transaction))
        return count / self.num_transactions
    
    def get_frequent_1_itemsets(self):
        """
        Generate frequent 1-itemsets
        
        Returns:
            dict: Dictionary of frequent 1-itemsets with their support
        """
        item_counts = defaultdict(int)
        
        # Count occurrences of each item
        for transaction in self.transactions:
            for item in transaction:
                item_counts[item] += 1
        
        # Filter items that meet minimum support
        frequent_1_itemsets = {}
        for item, count in item_counts.items():
            support = count / self.num_transactions
            if support >= self.min_support:
                frequent_1_itemsets[frozenset([item])] = support
        
        return frequent_1_itemsets
    
    def generate_candidates(self, frequent_itemsets_prev, k):
        """
        Generate candidate k-itemsets from frequent (k-1)-itemsets
        
        Args:
            frequent_itemsets_prev (dict): Frequent (k-1)-itemsets
            k (int): Size of itemsets to generate
            
        Returns:
            list: List of candidate k-itemsets
        """
        candidates = []
        itemsets = list(frequent_itemsets_prev.keys())
        
        for i in range(len(itemsets)):
            for j in range(i + 1, len(itemsets)):
                # Join two (k-1)-itemsets if they differ by only one item
                union = itemsets[i] | itemsets[j]
                if len(union) == k:
                    candidates.append(union)
        
        return candidates
    
    def prune_candidates(self, candidates, frequent_itemsets_prev):
        """
        Prune candidates that have infrequent subsets
        
        Args:
            candidates (list): List of candidate itemsets
            frequent_itemsets_prev (dict): Frequent (k-1)-itemsets
            
        Returns:
            list: Pruned list of candidates
        """
        pruned_candidates = []
        
        for candidate in candidates:
            # Check if all (k-1)-subsets are frequent
            subsets = [frozenset(s) for s in combinations(candidate, len(candidate) - 1)]
            if all(subset in frequent_itemsets_prev for subset in subsets):
                pruned_candidates.append(candidate)
        
        return pruned_candidates
    
    def find_frequent_itemsets(self):
        """
        Find all frequent itemsets using Apriori algorithm
        
        Returns:
            dict: Dictionary where keys are itemset sizes and values are frequent itemsets
        """
        self.frequent_itemsets = {}
        
        # Generate frequent 1-itemsets
        frequent_1_itemsets = self.get_frequent_1_itemsets()
        if not frequent_1_itemsets:
            return self.frequent_itemsets
        
        self.frequent_itemsets[1] = frequent_1_itemsets
        k = 2
        
        while True:
            # Generate candidates
            candidates = self.generate_candidates(self.frequent_itemsets[k-1], k)
            
            if not candidates:
                break
            
            # Prune candidates
            candidates = self.prune_candidates(candidates, self.frequent_itemsets[k-1])
            
            # Calculate support for candidates
            frequent_k_itemsets = {}
            for candidate in candidates:
                support = self.get_support(candidate)
                if support >= self.min_support:
                    frequent_k_itemsets[candidate] = support
            
            if not frequent_k_itemsets:
                break
            
            self.frequent_itemsets[k] = frequent_k_itemsets
            k += 1
        
        return self.frequent_itemsets
    
    def generate_association_rules(self):
        """
        Generate association rules from frequent itemsets
        
        Returns:
            list: List of association rules with confidence and lift
        """
        self.association_rules = []
        
        # Generate rules from itemsets with size >= 2
        for k in range(2, len(self.frequent_itemsets) + 1):
            for itemset, support in self.frequent_itemsets[k].items():
                # Generate all possible antecedent-consequent pairs
                for i in range(1, len(itemset)):
                    for antecedent in combinations(itemset, i):
                        antecedent = frozenset(antecedent)
                        consequent = itemset - antecedent
                        
                        # Calculate confidence
                        antecedent_support = self.get_support(antecedent)
                        confidence = support / antecedent_support
                        
                        if confidence >= self.min_confidence:
                            # Calculate lift
                            consequent_support = self.get_support(consequent)
                            lift = confidence / consequent_support
                            
                            rule = {
                                'antecedent': antecedent,
                                'consequent': consequent,
                                'support': support,
                                'confidence': confidence,
                                'lift': lift
                            }
                            self.association_rules.append(rule)
        
        return self.association_rules
    
    # def print_frequent_itemsets(self):
    #     """Print frequent itemsets"""
    #     print("Frequent Itemsets:")
    #     print("-" * 50)
        
    #     for k in sorted(self.frequent_itemsets.keys()):
    #         print(f"\n{k}-itemsets:")
    #         for itemset, support in self.frequent_itemsets[k].items():
    #             items = ', '.join(sorted(list(itemset)))
    #             print(f"  {{{items}}} - Support: {support:.3f}")
                
                
    def print_frequent_itemsets(self):
        """Print frequent itemsets"""
        result = "Frequent Itemsets:\n"
        result += "-" * 40 + "\n"
        
        for k in sorted(self.frequent_itemsets.keys()):
            result += f"\n{k}-itemsets:\n"
            for itemset, support in self.frequent_itemsets[k].items():
                items = ', '.join(sorted(list(itemset)))
                result += f"  {{{items}}} - Support: {support:.3f}\n"
        print(result)
        return result
    
    # def print_association_rules(self):
    #     """Print association rules"""
    #     print("\nAssociation Rules:")
    #     print("-" * 50)
        
    #     for rule in self.association_rules:
    #         antecedent = ', '.join(sorted(list(rule['antecedent'])))
    #         consequent = ', '.join(sorted(list(rule['consequent'])))
            
    #         print(f"{{{antecedent}}} -> {{{consequent}}}")
    #         print(f"  Support: {rule['support']:.3f}")
    #         print(f"  Confidence: {rule['confidence']:.3f}")
    #         print(f"  Lift: {rule['lift']:.3f}")
    #         print()
    
    def print_association_rules(self):
        """Print association rules"""
        result = "\nAssociation Rules:\n"
        result += "-" * 50 + "\n"
        
        for rule in self.association_rules:
            antecedent = ', '.join(sorted(list(rule['antecedent'])))
            consequent = ', '.join(sorted(list(rule['consequent'])))
            
            result += f"{{{antecedent}}} -> {{{consequent}}}\n"
            result += f"  Support: {rule['support']:.3f}\n"
            result += f"  Confidence: {rule['confidence']:.3f}\n"
            result += f"  Lift: {rule['lift']:.3f}\n"
            result += "\n"
        print(result)
        return result
