import { useState } from "react"

const ExampleComponent2: React.FC = () => {

    const [text, setTexto] = useState('')
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {

        setTexto(event.target.value)

    }

    return (
        <>
            <b>Digite um Texto:</b> <br />
            <input type="text" onBlur={handleChange} /> <br />
            <input type="text" onChange={handleChange} />
            <p><b>Conteúdo Digitado: {text}</b></p>
        </>
    )
}

export default ExampleComponent2