from deephyper.benchmark import NaProblem

from nas_problems.polynome2.load_data import load_data
from nas_problems.polynome2.preprocessing import minmaxstdscaler
from nas_problems.polynome2.structure import create_structure

Problem = NaProblem()

Problem.load_data(load_data, size=1e4)

Problem.preprocessing(minmaxstdscaler)

Problem.search_space(create_structure)

Problem.hyperparameters(
    batch_size=128,
    learning_rate=0.001,
    optimizer='rmsprop',
    num_epochs=5,
)

Problem.loss('mse')

Problem.metrics(['r2'])

Problem.objective('val_r2__last')

if __name__ == '__main__':
    print(Problem)