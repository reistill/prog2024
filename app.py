from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/listar_animais")
def listar_animais():
    with db_session:
        # obtém os animais
        animais = Animal.select() 
        return render_template("listar_animais.html", animais=animais)

@app.route("/form_adicionar_animal")
def form_adicionar_animal():
    return render_template("form_adicionar_animal.html")

@app.route("/adicionar_animal")
def adicionar_animal():
    # obter os parâmetros
    nome = request.args.get("nome")
    alimentacao = request.args.get("alimentacao")
    sexo = request.args.get("sexo")
    idade= request.args.get("idade")
    especie = request.args.get("especie")
    # salvar
    with db_session:
        # criar o animal
        a = Animal(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_animais")

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
    return redirect(url_for('listar_animais'))

app.run(debug=True)