import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import Projects from './Projects';

describe('Projects', () => {
  it('renders section title', () => {
    render(<Projects />);
    expect(screen.getByText('Proyectos Recientes')).toBeDefined();
  });

  it('renders all 6 projects', () => {
    render(<Projects />);
    expect(screen.getByText('Corporate Headquarters')).toBeDefined();
    expect(screen.getByText('Tech Campus Expansion')).toBeDefined();
    expect(screen.getByText('Financial Center Renovation')).toBeDefined();
    expect(screen.getByText('Healthcare Corp HQ')).toBeDefined();
    expect(screen.getByText('Law Firm Office')).toBeDefined();
    expect(screen.getByText('Startup Innovation Hub')).toBeDefined();
  });

  it('renders project locations', () => {
    render(<Projects />);
    expect(screen.getByText('Atlanta, GA')).toBeDefined();
    expect(screen.getByText('Alpharetta, GA')).toBeDefined();
    expect(screen.getByText('Midtown Atlanta')).toBeDefined();
  });

  it('renders "Ver Todos los Proyectos" button', () => {
    render(<Projects />);
    expect(screen.getByText('Ver Todos los Proyectos')).toBeDefined();
  });
});