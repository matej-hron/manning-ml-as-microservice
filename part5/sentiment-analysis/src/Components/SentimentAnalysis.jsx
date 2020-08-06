import React from 'react';
import { useState } from 'react';
import Axios from 'axios';

const SentimentAnalysis = () => {
    const [input, setInput] = useState("")
    const [sentiment, setSentiment] = useState("neutral")

    const evaluateInput = async () => {
        console.log(input)
        //const result = await Axios.get(`http://sentiment-analysis-369131487.eu-west-1.elb.amazonaws.com/predict?input=${encodeURI(input)}`)
        const result = await Axios.post(`http://sentiment-analysis-369131487.eu-west-1.elb.amazonaws.com/predict`, { input: input })
        console.log(result.data);
        setSentiment(result.data)

    }

    return (<>
        <textarea cols={80} rows={20} value={input} onChange={(x) => { setInput(x.target.value) }} style={{ backgroundColor: sentiment === "pos" ? "green" : sentiment === "neg" ? "red" : "white" }}></textarea>
        <button onClick={evaluateInput}>Send</button>
    </>)
}

export default SentimentAnalysis