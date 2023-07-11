import React, {useEffect, useState} from "react";
import Continent from "./Continent";

function BelongsFocus({focusBelongs, continentFocusSelector}) {

    const [filteredContinents, setFilteredContinents] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:7001/continents')
        .then(res => res.json())
        .then(allContinents => {
            let filteredContinents = []
            for (let i = 0; i < allContinents.length; i++) {
                let continent = allContinents[i]
                if (continent.belongs === focusBelongs) {
                    filteredContinents.push(continent)
                }
            }
            setFilteredContinents(filteredContinents)
        })
    }, [])

    const continent = filteredContinents.map((continent) => {
        return <Continent key={continent.id} continent={continent} continentFocusSelector={continentFocusSelector}/>
    })

    return(
        <div>
            <h2 className="belongs-title">Continents from: {focusBelongs}</h2>
            <div className="continents-grid">
                {continent}
            </div>
        </div>
    )
}

export default BelongsFocus