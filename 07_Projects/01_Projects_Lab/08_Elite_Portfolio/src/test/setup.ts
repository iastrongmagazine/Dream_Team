import { vi } from "vitest";

export const setup = () => {
  // Mock IntersectionObserver
  vi.stubGlobal("IntersectionObserver", vi.fn(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
})));

  // Mock matchMedia
  vi.stubGlobal("matchMedia", vi.fn((query: string) => ({
  matches: false,
  media: query,
  onchange: null,
  addListener: vi.fn(),
  removeListener: vi.fn(),
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  dispatchEvent: vi.fn(),
})));

  // Mock prefers-reduced-motion
  vi.stubGlobal("window", {
    ...window,
    matchMedia: vi.fn((query: string) => ({
      matches: query === "(prefers-reduced-motion: reduce)",
      media: query,
      onchange: null,
      addListener: vi.fn(),
      removeListener: vi.fn(),
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
      dispatchEvent: vi.fn(),
    })),
  });
};

export const teardown = () => {
  vi.unstubAllGlobals();
};