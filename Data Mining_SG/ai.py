import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def readData():
    
    transactions = []
    file = open("data.txt", 'r')
    for line in file:
    
        # Remove trailing comma and split by comma
        items = line.rstrip(',').split(',')
        num_items = len(items)
        total_quantity = 0
        
        # Parse each item:quantity pair
        for item in items:
            if ':' in item:
                _, quantity = item.split(':')
                total_quantity += int(quantity)
        
        transactions.append([num_items, total_quantity])
        
    return transactions
    # print(transactions)
    
def readDataLine():
        data_lines = []
        file = open("data.txt", 'r')
        i = 1
        for line in file:
            
            data_lines.append(str(i))
            i = i+1
            
        return data_lines   


######################################################################          
def kmean_clustering():
    
    data_points = readDataLine()
    data = np.array(readData())
    
    best_k = 2
    kmeans = KMeans(n_clusters=best_k,
    random_state=42, n_init=10)
    assignments = kmeans.fit_predict(data)
    centroids = kmeans.cluster_centers_

    
    
    # Create the plot
    plt.figure(figsize=(5, 4))
    
    # Define colors for different clusters
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    
    # Plot each cluster with different colors
    for i in range(best_k):
        cluster_points = data[assignments == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                  c=colors[i], label=f'Cluster {i}', s=100, alpha=0.7)
    
    # Plot centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], 
              c='black', marker='x', s=200, linewidths=3, label='Centroids')
    
    # Add data_point labels to points
    for i, data_point in enumerate(data_points):
        plt.annotate(data_point, (data[i, 0], data[i, 1]), 
                    xytext=(5, 5), textcoords='offset points')
    
    # Customize the plot
    plt.xlabel('Feature 1 total items')
    plt.ylabel('Feature 2 number of items')
    plt.title('K-means Clustering of customers')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Show the plot
    plt.tight_layout()
    # Show plot for 5 seconds then close automatically
    plt.show(block=False)
    plt.pause(4)
    plt.close()
    
    print(assignments)
    print(centroids)