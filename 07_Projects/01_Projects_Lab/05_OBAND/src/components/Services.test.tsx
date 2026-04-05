import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import Services from './Services';

describe('Services', () => {
  it('renders section title', () => {
    render(<Services />);
    expect(screen.getByText('Nuestros Servicios')).toBeDefined();
  });

  it('renders all 4 service cards', () => {
    render(<Services />);
    expect(screen.getByText('Amueblamiento Corporativo')).toBeDefined();
    expect(screen.getByText('Diseno de Espacios')).toBeDefined();
    expect(screen.getByText('Gestion de Proyectos')).toBeDefined();
    expect(screen.getByText('Logistica e Instalacion')).toBeDefined();
  });

  it('renders service descriptions', () => {
    render(<Services />);
    expect(screen.getByText(/Seleccion y suministro/)).toBeDefined();
    expect(screen.getByText(/Planificacion y distribucion/)).toBeDefined();
    expect(screen.getByText(/Coordinacion integral/)).toBeDefined();
    expect(screen.getByText(/Transporte, montje/)).toBeDefined();
  });
});