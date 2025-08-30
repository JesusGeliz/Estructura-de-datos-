class persona{
    constructor(this, nombre:Text , edad: Number){
        this.nombre = nombre;
        this.edad = edad; 
    }

    function saludar (this) {
        return "mi nombre es {this.nombre"
    }
}