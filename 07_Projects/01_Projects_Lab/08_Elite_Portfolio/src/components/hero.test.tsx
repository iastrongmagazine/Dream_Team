import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Hero } from "./hero";

vi.mock("next/font/google", () => ({
  Playfair_Display: () => ({ className: "font-serif" }),
  Inter: () => ({ className: "font-sans" }),
}));

describe("Hero Component", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("✅ RED: Renderiza el componente Hero con título", () => {
    // Given: El componente Hero existe
    // When: Se renderiza
    render(<Hero name="Test User" role="Designer" />);
    // Then: Muestra el nombre
    expect(screen.getByText("Test User")).toBeDefined();
  });

  it("✅ GREEN: Muestra el rol correctamente", () => {
    render(<Hero name="Test User" role="Designer" />);
    expect(screen.getByText("Designer")).toBeDefined();
  });

  it("✅ RED: Muestra tagline del componente", () => {
    render(<Hero name="Test User" role="Designer" tagline="Creating beautiful experiences" />);
    expect(screen.getByText("Creating beautiful experiences")).toBeDefined();
  });
});