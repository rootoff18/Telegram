package org.verdgram.messenger;

public interface GenericProvider<F, T> {
    T provide(F obj);
}
