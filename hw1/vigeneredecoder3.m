alpha=('abcdefghijklmnopqrstuvwxyz');
chitex='wynslzlwtomuxwbvvajkwyns';
zzchinum=zeros(1,24);
%try random keys, look for numbers (one two three..) in the output 
keylength = 5;
keynum=zeros(1,keylength);
message=zeros(1,24);
counter=zeros(1,26);

for i = 1:24
    for k = 1:26
        if strcmp(chitex(i),alpha(k))
            zzchinum(i)=k;
        end
    end
end

for w = 1:26
    for x = 1:26
        for y = 1:26
            for z = 1:26
                for za = 1:26
                
                key = [alpha(w) alpha(x) alpha(y) alpha(z) alpha(za)];

for i = 1:keylength
    for k = 1:26
        if strcmp(key(i),alpha(k))
            keynum(i)=k;
        end
    end
end

for i = 1:24
    k=i;
    while k>keylength
        k=k-keylength;
    end 
    
    message(i)=zzchinum(i)-keynum(k);
        
end
%fix message for neg numbers

for i = 1:24
    if message(i) <= 0
        message(i) = message(i)+26;
    end
end

for i = 1:24
    beta(i)=alpha(message(i));
end
betasnip = beta(1:4);
if contains(betasnip,["zero","four","five","nine"])
    clc
    disp(beta)
end
                end
            end
        end
    end
end