function x = gaussian_elimination_band(A, b, W)
    N = length(b);
    A = double(A);
    b = double(b);

    % Implement gaussian elimination
    for i = 1:N
        pivot = A(i, i);
        if pivot == 0
            error('Zero pivot encountered!');
        end
        for j = i+1 : min(i + W, N)
            factor = A(j, i) / pivot;
            A(j, i:min(i + W, N)) = A(j, i:min(i + W, N)) - factor * A(i, i:min(i + W, N));
            b(j) = b(j) - factor * b(i);
        end
    end

    % Use back Substitution for the result
    x = zeros(N, 1);
    for i = N:-1:1
        x(i) = (b(i) - A(i, i+1:min(i + W, N)) * x(i+1:min(i + W, N))) / A(i, i);
    end
end
