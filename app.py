from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    with db_session:
        # obtém as pessoas
        animais = Animal.select() 
        return render_template("listar_pessoas.html", animais=animais)

@app.route("/form_adicionar_pessoa")
def form_adicionar_pessoa():
    return render_template("form_adicionar_pessoa.html")

@app.route("/adicionar_pessoa")
def adicionar_pessoa():
    # obter os parâmetros
    nome = request.args.get("nome")
    alimentacao = request.args.get("alimentacao")
    sexo = request.args.get("sexo")
    idade= request.args.get("idade")
    especie = request.args.get("especie")
    # salvar
    with db_session:
        # criar a pessoa
        a = Animal(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_pessoas")

#usei chat gpt nessa parte
@app.route("/excluir_animal/<int:id>", methods=['POST'])
@db_session
def excluir_animal(id):
    try:
        animal = Animal.get(id=id)
        if animal:
            animal.delete()
            commit()
            app.logger.info(f"Animal with ID {id} deleted successfully.")
        else:
            app.logger.warning(f"Animal with ID {id} not found.")
            return render_template("error.html", message="Animal não encontrado")
    except Exception as e:
        app.logger.error(f"Error deleting animal with ID {id}: {str(e)}")
        return render_template("error.html", message=str(e))
    return redirect(url_for('listar_pessoas'))

app.run(debug=True)