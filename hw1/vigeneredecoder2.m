function [] = vigeneredecoder2(key,ciphertext)
%This function takes in text encrypted with vigenere cipher and a key and
%decodes the message

alpha=('abcdefghijklmnopqrstuvwxyz');

%chitext=('uncfdvaztcdpdyzjhrcfvyhj');
chitext = ciphertext;
chilength = length(chitext);
chinum=zeros(1,chilength);

%key=('bigapple');
keylength = length(key);
keynum=zeros(1,keylength);

message=zeros(1,chilength);
counter=zeros(1,26);

for i = 1:chilength
    for k = 1:26
        if strcmp(chitext(i),alpha(k))
            chinum(i)=k;
        end
    end
end

for i = 1:keylength
    for k = 1:26
        if strcmp(key(i),alpha(k))
            keynum(i)=k;
        end
    end
end

for i = 1:chilength
    k=i;
    while k>keylength
        k=k-keylength;
    end 
    
    message(i)=chinum(i)-keynum(k);
        
end

for i = 1:24
    if message(i) <= 0
        message(i) = message(i)+26;
    end
end

for i = 1:24
    beta(i)=alpha(message(i));
end

disp(beta)

end