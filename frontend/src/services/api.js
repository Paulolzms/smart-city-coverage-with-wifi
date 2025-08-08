import axios from 'axios';

export const generateGraph = async (city, distance) => {
  try {
    const res = await axios.post('http://localhost:5000/generate-graph', {
      city,
      distance
    });
    return res.data;
  } catch (error) {
    console.error("Erro ao gerar grafo:", error);
    return null;
  }
}