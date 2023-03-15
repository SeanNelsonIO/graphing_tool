import matplotlib.pyplot as plt
import csv

def choose_plotting_function(plotting_function, csv_file_name) -> None:
    if plotting_function == 'mouse':
        plot_mouse_graph(csv_file_name)
    if plotting_function == 'chase':
        plot_chase_graph(csv_file_name)
    else:
        return None


def plot_chase_graph(csv_file_name: str) -> None:
    # Initialize lists to store the fitness values
    prey_average_fitness = []
    prey_best_fitness = []

    predator_average_fitness = []
    predator_best_fitness = []
        
    # Open the input file and read the data
    with open("csv_data/{}".format(csv_file_name), 'r') as input_file:
        # Process each row in the CSV file
        csv_reader = csv.reader(input_file)
        line_counter = 1
        for row in csv_reader:
            if line_counter % 2 == 0:
                prey_average_fitness.append(float(row[1]))
                prey_best_fitness.append(float(row[2]))
            else:
                predator_average_fitness.append(float(row[1]))
                predator_best_fitness.append(float(row[2]))
            
            line_counter = line_counter + 1



    # Plot the fitness values
    generations = range(1, len(predator_average_fitness) + 1)

    plt.plot(generations, prey_average_fitness, label='prey Average fitness')
    plt.plot(generations, prey_best_fitness, label='Prey Best fitness')

    plt.plot(generations, predator_average_fitness, label='Predator Average fitness')
    plt.plot(generations, predator_best_fitness, label='Predator Best fitness')

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




def plot_mouse_graph(csv_file_name: str) -> None:
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
