from program.model.Model import Model
from program.presenter.Presenter import Presenter
from program.view.ConsoleUI import ConsoleUI

if __name__ == '__main__':
    model = Model()
    console = ConsoleUI()
    presenter = Presenter(console, model)
    console.set_presenter(presenter)
    console.start()

