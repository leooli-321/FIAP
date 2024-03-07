import React, { useState } from "react";

const ExampleComponent: React.FC = () => {

    const [count, setCount] = useState(0)

    const counter = () => {
        setCount(count + 1)
    }

    return (
        <>
            <button onClick={counter}>Aperte aqui</button>
            <p>Contador: {count}</p>
        </>
    )
}

export default ExampleComponent