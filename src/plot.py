import matplotlib.pyplot as plt
import csv

def plot_graph(csv_file_name: str) -> None:
    # Initialize lists to store the fitness values
    average_fitness = []
    best_fitness = []
        
    # Open the input file and read the data
    with open("csv_data/{}".format(csv_file_name), 'r') as input_file:
        # Process each row in the CSV file
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            average_fitness.append(float(row[1]))
            best_fitness.append(float(row[2]))


    # Plot the fitness values
    generations = range(1, len(average_fitness) + 1)
    plt.plot(generations, average_fitness, label='Average fitness')
    plt.plot(generations, best_fitness, label='Best fitness')

    # Add labels and a legend to the plot
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness over generations')
    plt.legend()


    file_name = csv_file_name[:-4]
    #save graph to directory
    plt.savefig('plots/{}.png'.format(file_name))

    # Display the plot
    plt.show()
