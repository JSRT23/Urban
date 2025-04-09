
  document.addEventListener('DOMContentLoaded', () => {
      const productosCamisas = document.querySelector('#camisas .productos');
      const productosVestidos = document.querySelector('#vestidos .productos');
      const productosZapatos = document.querySelector('#zapatos .productos');
    
      const productos = [
        { nombre: 'Camisa Blanca', categoria: 'camisas', precio: 25 },
        { nombre: 'Camisa Azul', categoria: 'camisas', precio: 30 },
        { nombre: 'Camisa Negra', categoria: 'camisas', precio: 27 },
        { nombre: 'Vestido Rojo', categoria: 'vestidos', precio: 45 },
        { nombre: 'Vestido Azul', categoria: 'vestidos', precio: 50 },
        { nombre: 'Vestido Verde', categoria: 'vestidos', precio: 48 },
        { nombre: 'Zapatos Deportivos', categoria: 'zapatos', precio: 60 },
        { nombre: 'Zapatos de Cuero', categoria: 'zapatos', precio: 75 },
        { nombre: 'Sandalias', categoria: 'zapatos', precio: 35 },
        { nombre: 'Botas Negras', categoria: 'zapatos', precio: 80 }
      ];
    
      productos.forEach(p => {
        const item = document.createElement('div');
        item.classList.add('producto');
        item.innerHTML = `
          <h4>${p.nombre}</h4>
          <p>Precio: $${p.precio}</p>
          <button class="agregar-carrito">Agregar al carrito</button>
        `;
    
        if (p.categoria === 'camisas') productosCamisas.appendChild(item);
        if (p.categoria === 'vestidos') productosVestidos.appendChild(item);
        if (p.categoria === 'zapatos') productosZapatos.appendChild(item);
      });
    });